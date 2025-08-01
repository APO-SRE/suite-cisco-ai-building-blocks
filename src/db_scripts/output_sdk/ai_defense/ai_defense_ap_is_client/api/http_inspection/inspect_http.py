from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.http_inspect_request import HttpInspectRequest
from ...models.inspect_response import InspectResponse
from ...types import Response


def _get_kwargs(
    *,
    body: HttpInspectRequest,
    x_cisco_ai_defense_api_key: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["X-Cisco-AI-Defense-API-Key"] = x_cisco_ai_defense_api_key

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/inspect/http",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Error, InspectResponse]]:
    if response.status_code == 200:
        response_200 = InspectResponse.from_dict(response.json())

        return response_200
    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())

        return response_401
    if response.status_code == 500:
        response_500 = Error.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Error, InspectResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: HttpInspectRequest,
    x_cisco_ai_defense_api_key: str,
) -> Response[Union[Error, InspectResponse]]:
    """Inspect an HTTP request or response

     The HTTP Inspect API allows network firewall products to submit GenAI-related HTTP requests and
    responses to AI Defense for inspection.

    Args:
        x_cisco_ai_defense_api_key (str):
        body (HttpInspectRequest): The request to inspect a HTTP request or HTTP response

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, InspectResponse]]
    """

    kwargs = _get_kwargs(
        body=body,
        x_cisco_ai_defense_api_key=x_cisco_ai_defense_api_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    body: HttpInspectRequest,
    x_cisco_ai_defense_api_key: str,
) -> Optional[Union[Error, InspectResponse]]:
    """Inspect an HTTP request or response

     The HTTP Inspect API allows network firewall products to submit GenAI-related HTTP requests and
    responses to AI Defense for inspection.

    Args:
        x_cisco_ai_defense_api_key (str):
        body (HttpInspectRequest): The request to inspect a HTTP request or HTTP response

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, InspectResponse]
    """

    return sync_detailed(
        client=client,
        body=body,
        x_cisco_ai_defense_api_key=x_cisco_ai_defense_api_key,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: HttpInspectRequest,
    x_cisco_ai_defense_api_key: str,
) -> Response[Union[Error, InspectResponse]]:
    """Inspect an HTTP request or response

     The HTTP Inspect API allows network firewall products to submit GenAI-related HTTP requests and
    responses to AI Defense for inspection.

    Args:
        x_cisco_ai_defense_api_key (str):
        body (HttpInspectRequest): The request to inspect a HTTP request or HTTP response

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, InspectResponse]]
    """

    kwargs = _get_kwargs(
        body=body,
        x_cisco_ai_defense_api_key=x_cisco_ai_defense_api_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: HttpInspectRequest,
    x_cisco_ai_defense_api_key: str,
) -> Optional[Union[Error, InspectResponse]]:
    """Inspect an HTTP request or response

     The HTTP Inspect API allows network firewall products to submit GenAI-related HTTP requests and
    responses to AI Defense for inspection.

    Args:
        x_cisco_ai_defense_api_key (str):
        body (HttpInspectRequest): The request to inspect a HTTP request or HTTP response

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, InspectResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            x_cisco_ai_defense_api_key=x_cisco_ai_defense_api_key,
        )
    ).parsed
