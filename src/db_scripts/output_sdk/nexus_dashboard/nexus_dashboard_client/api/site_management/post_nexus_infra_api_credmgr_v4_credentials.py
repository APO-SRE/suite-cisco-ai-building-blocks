from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.credential_v4_credmgr_get import CredentialV4CredmgrGET
from ...models.credential_v4_credmgr_post import CredentialV4CredmgrPOST
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: CredentialV4CredmgrPOST,
    auth_cookie: Union[Unset, str] = UNSET,
    cookie: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(auth_cookie, Unset):
        headers["AuthCookie"] = auth_cookie

    if not isinstance(cookie, Unset):
        headers["Cookie"] = cookie

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/nexus/infra/api/credmgr/v4/credentials",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, CredentialV4CredmgrGET]]:
    if response.status_code == 201:
        response_201 = CredentialV4CredmgrGET.from_dict(response.json())

        return response_201
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
) -> Response[Union[Any, CredentialV4CredmgrGET]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: CredentialV4CredmgrPOST,
    auth_cookie: Union[Unset, str] = UNSET,
    cookie: Union[Unset, str] = UNSET,
) -> Response[Union[Any, CredentialV4CredmgrGET]]:
    """Create an existing object of type Credential

    Args:
        auth_cookie (Union[Unset, str]):
        cookie (Union[Unset, str]):
        body (CredentialV4CredmgrPOST):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, CredentialV4CredmgrGET]]
    """

    kwargs = _get_kwargs(
        body=body,
        auth_cookie=auth_cookie,
        cookie=cookie,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    body: CredentialV4CredmgrPOST,
    auth_cookie: Union[Unset, str] = UNSET,
    cookie: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, CredentialV4CredmgrGET]]:
    """Create an existing object of type Credential

    Args:
        auth_cookie (Union[Unset, str]):
        cookie (Union[Unset, str]):
        body (CredentialV4CredmgrPOST):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, CredentialV4CredmgrGET]
    """

    return sync_detailed(
        client=client,
        body=body,
        auth_cookie=auth_cookie,
        cookie=cookie,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: CredentialV4CredmgrPOST,
    auth_cookie: Union[Unset, str] = UNSET,
    cookie: Union[Unset, str] = UNSET,
) -> Response[Union[Any, CredentialV4CredmgrGET]]:
    """Create an existing object of type Credential

    Args:
        auth_cookie (Union[Unset, str]):
        cookie (Union[Unset, str]):
        body (CredentialV4CredmgrPOST):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, CredentialV4CredmgrGET]]
    """

    kwargs = _get_kwargs(
        body=body,
        auth_cookie=auth_cookie,
        cookie=cookie,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: CredentialV4CredmgrPOST,
    auth_cookie: Union[Unset, str] = UNSET,
    cookie: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, CredentialV4CredmgrGET]]:
    """Create an existing object of type Credential

    Args:
        auth_cookie (Union[Unset, str]):
        cookie (Union[Unset, str]):
        body (CredentialV4CredmgrPOST):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, CredentialV4CredmgrGET]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            auth_cookie=auth_cookie,
            cookie=cookie,
        )
    ).parsed
