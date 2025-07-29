from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.gateway_configuration_v4_aaa_get import GatewayConfigurationV4AaaGET
from ...models.gateway_configuration_v4_aaa_put import GatewayConfigurationV4AaaPUT
from ...types import UNSET, Response, Unset


def _get_kwargs(
    spec_name: str,
    *,
    body: GatewayConfigurationV4AaaPUT,
    auth_cookie: Union[Unset, str] = UNSET,
    cookie: Union[Unset, str] = UNSET,
    x_csrf_token: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(auth_cookie, Unset):
        headers["AuthCookie"] = auth_cookie

    if not isinstance(cookie, Unset):
        headers["Cookie"] = cookie

    if not isinstance(x_csrf_token, Unset):
        headers["X-Csrf-Token"] = x_csrf_token

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/nexus/infra/api/aaa/v4/gatewayconfiguration/{spec_name}",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, GatewayConfigurationV4AaaGET]]:
    if response.status_code == 200:
        response_200 = GatewayConfigurationV4AaaGET.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400
    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403
    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404
    if response.status_code == 429:
        response_429 = cast(Any, None)
        return response_429
    if response.status_code == 500:
        response_500 = cast(Any, None)
        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, GatewayConfigurationV4AaaGET]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    spec_name: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: GatewayConfigurationV4AaaPUT,
    auth_cookie: Union[Unset, str] = UNSET,
    cookie: Union[Unset, str] = UNSET,
    x_csrf_token: Union[Unset, str] = UNSET,
) -> Response[Union[Any, GatewayConfigurationV4AaaGET]]:
    """Modify a gateway configuration

     Modify a resource of type GatewayConfiguration

    Args:
        spec_name (str):
        auth_cookie (Union[Unset, str]):
        cookie (Union[Unset, str]):
        x_csrf_token (Union[Unset, str]):
        body (GatewayConfigurationV4AaaPUT): API Gateway Configuration Resource

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GatewayConfigurationV4AaaGET]]
    """

    kwargs = _get_kwargs(
        spec_name=spec_name,
        body=body,
        auth_cookie=auth_cookie,
        cookie=cookie,
        x_csrf_token=x_csrf_token,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    spec_name: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: GatewayConfigurationV4AaaPUT,
    auth_cookie: Union[Unset, str] = UNSET,
    cookie: Union[Unset, str] = UNSET,
    x_csrf_token: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, GatewayConfigurationV4AaaGET]]:
    """Modify a gateway configuration

     Modify a resource of type GatewayConfiguration

    Args:
        spec_name (str):
        auth_cookie (Union[Unset, str]):
        cookie (Union[Unset, str]):
        x_csrf_token (Union[Unset, str]):
        body (GatewayConfigurationV4AaaPUT): API Gateway Configuration Resource

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GatewayConfigurationV4AaaGET]
    """

    return sync_detailed(
        spec_name=spec_name,
        client=client,
        body=body,
        auth_cookie=auth_cookie,
        cookie=cookie,
        x_csrf_token=x_csrf_token,
    ).parsed


async def asyncio_detailed(
    spec_name: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: GatewayConfigurationV4AaaPUT,
    auth_cookie: Union[Unset, str] = UNSET,
    cookie: Union[Unset, str] = UNSET,
    x_csrf_token: Union[Unset, str] = UNSET,
) -> Response[Union[Any, GatewayConfigurationV4AaaGET]]:
    """Modify a gateway configuration

     Modify a resource of type GatewayConfiguration

    Args:
        spec_name (str):
        auth_cookie (Union[Unset, str]):
        cookie (Union[Unset, str]):
        x_csrf_token (Union[Unset, str]):
        body (GatewayConfigurationV4AaaPUT): API Gateway Configuration Resource

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GatewayConfigurationV4AaaGET]]
    """

    kwargs = _get_kwargs(
        spec_name=spec_name,
        body=body,
        auth_cookie=auth_cookie,
        cookie=cookie,
        x_csrf_token=x_csrf_token,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    spec_name: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: GatewayConfigurationV4AaaPUT,
    auth_cookie: Union[Unset, str] = UNSET,
    cookie: Union[Unset, str] = UNSET,
    x_csrf_token: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, GatewayConfigurationV4AaaGET]]:
    """Modify a gateway configuration

     Modify a resource of type GatewayConfiguration

    Args:
        spec_name (str):
        auth_cookie (Union[Unset, str]):
        cookie (Union[Unset, str]):
        x_csrf_token (Union[Unset, str]):
        body (GatewayConfigurationV4AaaPUT): API Gateway Configuration Resource

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GatewayConfigurationV4AaaGET]
    """

    return (
        await asyncio_detailed(
            spec_name=spec_name,
            client=client,
            body=body,
            auth_cookie=auth_cookie,
            cookie=cookie,
            x_csrf_token=x_csrf_token,
        )
    ).parsed
