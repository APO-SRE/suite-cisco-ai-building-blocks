from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.member_v4_federation_get import MemberV4FederationGET
from ...types import UNSET, Response, Unset


def _get_kwargs(
    status_member_id: str,
    *,
    auth_cookie: Union[Unset, str] = UNSET,
    cookie: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(auth_cookie, Unset):
        headers["AuthCookie"] = auth_cookie

    if not isinstance(cookie, Unset):
        headers["Cookie"] = cookie

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/nexus/api/federation/v4/members/{status_member_id}",
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, MemberV4FederationGET]]:
    if response.status_code == 200:
        response_200 = MemberV4FederationGET.from_dict(response.json())

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
) -> Response[Union[Any, MemberV4FederationGET]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    status_member_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    auth_cookie: Union[Unset, str] = UNSET,
    cookie: Union[Unset, str] = UNSET,
) -> Response[Union[Any, MemberV4FederationGET]]:
    """Get a federation member

     Get a resource of type Federation Member

    Args:
        status_member_id (str):
        auth_cookie (Union[Unset, str]):
        cookie (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, MemberV4FederationGET]]
    """

    kwargs = _get_kwargs(
        status_member_id=status_member_id,
        auth_cookie=auth_cookie,
        cookie=cookie,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    status_member_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    auth_cookie: Union[Unset, str] = UNSET,
    cookie: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, MemberV4FederationGET]]:
    """Get a federation member

     Get a resource of type Federation Member

    Args:
        status_member_id (str):
        auth_cookie (Union[Unset, str]):
        cookie (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, MemberV4FederationGET]
    """

    return sync_detailed(
        status_member_id=status_member_id,
        client=client,
        auth_cookie=auth_cookie,
        cookie=cookie,
    ).parsed


async def asyncio_detailed(
    status_member_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    auth_cookie: Union[Unset, str] = UNSET,
    cookie: Union[Unset, str] = UNSET,
) -> Response[Union[Any, MemberV4FederationGET]]:
    """Get a federation member

     Get a resource of type Federation Member

    Args:
        status_member_id (str):
        auth_cookie (Union[Unset, str]):
        cookie (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, MemberV4FederationGET]]
    """

    kwargs = _get_kwargs(
        status_member_id=status_member_id,
        auth_cookie=auth_cookie,
        cookie=cookie,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    status_member_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    auth_cookie: Union[Unset, str] = UNSET,
    cookie: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, MemberV4FederationGET]]:
    """Get a federation member

     Get a resource of type Federation Member

    Args:
        status_member_id (str):
        auth_cookie (Union[Unset, str]):
        cookie (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, MemberV4FederationGET]
    """

    return (
        await asyncio_detailed(
            status_member_id=status_member_id,
            client=client,
            auth_cookie=auth_cookie,
            cookie=cookie,
        )
    ).parsed
